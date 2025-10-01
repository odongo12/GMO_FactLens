import asyncio
import re
from typing import Dict, List, Optional
import httpx
import streamlit as st


class LinkedInScraper:
    """
    Lightweight scraper for public LinkedIn post pages.

    Notes:
    - We avoid heavy dependencies and login; only public content is attempted.
    - Uses simple HTML extraction heuristics; best-effort only.
    - Non-fatal on errors; returns empty list to avoid breaking pipeline.
    """

    def __init__(self, timeout_seconds: float = 15.0) -> None:
        self.timeout_seconds = timeout_seconds

    async def _fetch(self, client: httpx.AsyncClient, url: str) -> Optional[str]:
        try:
            resp = await client.get(url, headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
            })
            if resp.status_code == 200:
                return resp.text
            return None
        except Exception as exc:
            st.warning(f"LinkedIn fetch failed for {url}: {str(exc)}")
            return None

    def _extract_text(self, html: str) -> str:
        # Heuristic: remove scripts/styles, collapse whitespace, try to locate post text patterns
        cleaned = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.IGNORECASE)
        cleaned = re.sub(r"<style[\s\S]*?</style>", " ", cleaned, flags=re.IGNORECASE)
        # Try to find JSON-LD description first
        m = re.search(r'"description"\s*:\s*"([^"]{20,})"', cleaned)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()

        # Fallback: strip tags and truncate
        text = re.sub(r"<[^>]+>", " ", cleaned)
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) > 2000:
            text = text[:2000] + "..."
        return text

    def _guess_title(self, html: str, url: str) -> str:
        m = re.search(r"<title>([^<]{5,})</title>", html, flags=re.IGNORECASE)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()
        return url

    async def scrape_posts_async(self, urls: List[str]) -> List[Dict[str, str]]:
        if not urls:
            return []

        timeout = httpx.Timeout(self.timeout_seconds)
        scraped: List[Dict[str, str]] = []
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            html_list = await asyncio.gather(*(self._fetch(client, u) for u in urls))

        for url, html in zip(urls, html_list):
            if not html:
                continue
            try:
                content = self._extract_text(html)
                if not content or len(content) < 80:
                    # Likely blocked or not enough text
                    continue
                title = self._guess_title(html, url)
                scraped.append({
                    "url": url,
                    "content": content,
                    "title": title
                })
            except Exception as exc:
                st.warning(f"LinkedIn parse failed for {url}: {str(exc)}")
                continue

        return scraped

    def scrape_posts(self, urls: List[str]) -> List[Dict[str, str]]:
        try:
            return asyncio.run(self.scrape_posts_async(urls))
        except RuntimeError:
            # In case we're already in an event loop (e.g., some environments)
            return asyncio.get_event_loop().run_until_complete(self.scrape_posts_async(urls))



import os
from typing import List
import requests
import streamlit as st


class LinkedInSearchAgent:
    """
    Searches LinkedIn posts via SerperAPI using a site-restricted query.

    Query pattern: "site:linkedin.com/posts {topic}"
    """

    def __init__(self) -> None:
        self.api_key = os.getenv("SERPER_API_KEY")
        self.base_url = "https://google.serper.dev/search"

    def search_linkedin_posts(self, topic: str, max_results: int = 3) -> List[str]:
        """
        Find LinkedIn post URLs for a given topic.

        Args:
            topic: The topic to search for
            max_results: Maximum number of results to return

        Returns:
            List of LinkedIn post URLs
        """
        if not self.api_key:
            # Keep behavior non-fatal
            st.warning("SERPER_API_KEY not found; skipping LinkedIn search")
            return []

        headers = {"X-API-KEY": self.api_key, "Content-Type": "application/json"}
        payload = {"q": f"site:linkedin.com/posts {topic}", "num": max_results}

        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            urls: List[str] = []
            if "organic" in data:
                for result in data["organic"][:max_results]:
                    link = result.get("link")
                    if isinstance(link, str) and "linkedin.com" in link:
                        urls.append(link)

            if urls:
                st.info(f"LinkedIn: found {len(urls)} URLs for '{topic}'")
            return urls

        except requests.exceptions.RequestException as exc:
            st.warning(f"LinkedIn search error: {str(exc)}")
            return []
        except Exception as exc:
            st.warning(f"Unexpected LinkedIn search error: {str(exc)}")
            return []



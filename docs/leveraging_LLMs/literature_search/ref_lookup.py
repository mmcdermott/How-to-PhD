import requests
import argparse

from typing import Optional, List

API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def search_papers(query: str, results_limit: int = 4) -> Optional[List[dict]]:
    """
    Search for academic papers using the Semantic Scholar API.

    Args:
        query (str): The search query.
        results_limit (int, optional): The maximum number of results to return. Defaults to 4.

    Returns:
        list: A list of dictionaries containing the search results.
    """
    params = {
        "query": query,
        "sort": "relevance",
        "limit": results_limit,
        'fields': 'title,abstract',
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return None

def display_results(search_query: str, results: List[dict], char_limit: int = 300):
    """
    Display the search results in a readable format.

    Args:
        search_query (str): The search query.
        results (list): A list of dictionaries containing the search results.
    """
    print(f"Query: '{search_query}'")
    for result in results:
        title = result["title"]
        print(f"Title: '{title}'")

        abstract = result.get("abstract", "")
        if abstract:
            print(f"Abstract: '{abstract[:char_limit]}'")
    print()

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Search Semantic Scholar for articles")
    parser.add_argument("queries", metavar="QUERY", nargs="+", help="search query")
    parser.add_argument("-n", "--num_results", type=int, default=4, help="number of results per query (default: 4)")
    parser.add_argument(
        "-c", "--char_limit", type=int, default=300,
        help="number of characters of the abstract to display per query (default: 300)"
    )
    args = parser.parse_args()

    # Perform the search and display the results
    for query in args.queries:
        results = search_papers(query, results_limit=args.num_results)
        if results:
            display_results(query, results, char_limit=args.char_limit)
        else:
            print(f"No results found for query: '{query}'")

if __name__ == "__main__":
    main()

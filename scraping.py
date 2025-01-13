from bs4 import BeautifulSoup
import requests
def scrape_parabank(url,in_site_links,out_of_site_links):
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    all_links=soup.find_all("a")
    
    for link in all_links:
        if "http" in link["href"] or "https" in link["href"]:
            out_of_site_links.append(link["href"])
        else:
            in_site_links.append(link["href"])    

def main():
    url="https://parabank.parasoft.com/parabank/index.htm"
    in_site_links=[]
    out_of_site_links=[]
    scrape_parabank(url,in_site_links,out_of_site_links)
    print("all links that leads to the same website:")
    set_in_site_links=set(in_site_links)
    set_out_of_site_links=set(out_of_site_links)
    for link in set_in_site_links:
        print(link)
    print("all links that leads outside the website:")
    for link in set_out_of_site_links:
        print(link)

    

if __name__ == "__main__":
    main()   
# CRAWLING DATA FROM WEB

from urllib.request import urlopen       as uReq
from bs4            import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'

## Opening up connection, grabbing page - mở kết nối, lấy trang
uClient   = uReq(my_url)
page_html = uClient.read()
uClient.close()

## HTML PARSING - phân tích cú pháp HTML
page_soup = soup(page_html, 'html.parser')

# Evaluating Web page
print(page_soup.h1)  # <h1> là thẻ tiêu đề website
print(page_soup.p)   # <p>  là thẻ giúp trình duyệt xác định được đoạn văn bản trong trang HTML

# Converting Listings into Lines Items
print(page_soup.body.span)
# grabs each product
containers = page_soup.findAll("div",
                               {"class": "item-container"})  # notice: the object that we need to findAll being in {})
print("\nThe number of products: ", len(containers))

# Creating csv file. Open & Write headers
filename = "products-info.csv"
file     = open(filename, "w")
headers  = "Brand, Product_name, Shipping\n"
file.write(headers)

# Extract data
for container in containers:
    brand              = container.div.div.a.img["title"]

    title_container    = container.findAll("a",{"class":"item-title"})

    product_name       = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping           = shipping_container[0].text.strip()      # strip() removes whitespaces before & after new lines

    print("Brand: " + brand)
    print("Product_name: " + product_name)
    print("Shipping: " + shipping)

    file.write(brand + ": " + product_name.replace(",", " ") + "- " + shipping + "\n")

# Close file
file.close()

import renderer
import lxml
# from bot import renderer

def main():
    render_a_page = renderer.Renderer()

    soup = render_a_page.get_soup()
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="price_inside_buybox").get_text().strip()
    print(f"Title is: {title}")
    print(f"Price is: {price}")



    # amazon_product_price = render_a_page.find_price()
    # print(f"amazon_product_price: {amazon_product_price}")

    amazon_product_price = render_a_page.find_price()
    print(f"amazon_product_price: {amazon_product_price}")


if __name__ == '__main__':
    main()
from lxml import etree

def get_rect_data(html_string):
    """
    Parses an HTML string, extracts data from <rect> elements, and calculates areas.

    Args:
        html_string: The HTML string to parse.

    Returns:
        A tuple containing a list of dictionaries (each with 'width', 'height', 'area') and the total area.  Returns ([], 0) if no rects are found or if an error occurs during parsing.
    """
    try:
        root = etree.HTML(html_string)
        rects = root.xpath("//rect")
        rect_data = []
        total_area = 0

        for rect in rects:
            width = rect.get("width")
            height = rect.get("height")
            try:
                width = float(width)
                height = float(height)
                area = width * height
                rect_data.append({"width": width, "height": height, "area": area})
                total_area += area
            except (ValueError, TypeError):
                print(f"Warning: Invalid width or height attribute for rect element: {etree.tostring(rect, encoding='unicode')}")

        return rect_data, total_area
    except etree.XMLSyntaxError:
        print("Error: Invalid HTML string.")
        return [], 0


# example of html string
html_string = """
<svg>
  <rect width="10" height="20" />
  <rect width="30" height="40" style="fill:blue;" />
  <rect width="50" height="60" fill="red"/>
  <rect width="abc" height="10"/>  <!--无效的rect-->
  <rect height="10"/> <!--无效的rect-->
</svg>
"""

rect_data, total_area = get_rect_data(html_string)
print("每个长方形的数据：", rect_data)
print("所有长方形的总面积：", total_area)

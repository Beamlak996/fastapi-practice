from fastapi import APIRouter, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional, List

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'phone', 'camera']
@router.get('/all')
def get_all_products():
    # return products
    data = " ".join(products)
    return Response(content=data, media_type='text/plain')

@router.get("/withheader")
def get_products(response: Response, custom_handle: Optional[List[str]] = Header(None)):
    return products

@router.get("/{id}", responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "descriptions": "Return html"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not found"
            }
        },
        "descriptions": "A clear text error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = "Product not found"
        return PlainTextResponse(status_code=404, content=out, media_type='text/plain')
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
                .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
                }}
            </style>
        </head>
        <div class="product" >{product}</div>
    """
        return HTMLResponse(content=out, media_type="text/html")
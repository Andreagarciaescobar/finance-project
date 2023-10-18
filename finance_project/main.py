"""Main module of finance Application"""

from typing import List
from fastapi import FastAPI, HTTPException

from finance_project.models.stocks import Stock
from finance_project.schemes.stocks_schemas import StockSchema

app = FastAPI()

stocks: List[Stock] = [
    Stock("Apple Company", 102, "AAPL.US"),
    Stock("Microsoft Company", 78, "MICRO.US"),
    Stock("Google Company", 92, "GGLE.US")

]

@app.get("/stocks")
def get_stocks():
    print(str(stocks))
    return stocks

@app.post("/stocks/create-stock")
def create_stocks(stock_body: StockSchema):
     stock = Stock(**stock_body.model_dump())
     stocks.append(stock)
     

@app.get("/stocks/get-stock/{stock_name}")
def get_stock_by_name(stock_name: str):
    for stock in stocks:
        if stock.name == stock_name:
            return stock
    raise HTTPException(status_code=404, detail="Stock not found")
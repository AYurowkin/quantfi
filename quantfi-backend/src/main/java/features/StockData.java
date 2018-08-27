package features;

import connection.ApiConnector;

// main class to pull in historical data of a given stock.

//TODO: need to rename for clarity

public class StockData {
    private final ApiConnector connector;

    public StockData(ApiConnector connector) {
        this.connector = connector;
    }
}

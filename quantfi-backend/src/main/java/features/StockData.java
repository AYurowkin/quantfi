package data;

import connection.ApiConnector;

public class StockData {
    private final ApiConnector connector;

    public StockData(ApiConnector connector) {
        this.connector = connector;
    }
}

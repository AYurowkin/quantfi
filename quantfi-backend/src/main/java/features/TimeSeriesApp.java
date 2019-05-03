package features;

import connection.AlphaVantageConnector;
import data.*;

// main class to send all requests to Alpha Vantage API
public class TimeSeriesApp {
    public static void main(String[] args) {
        // set key, timeout, connection to Alpha Vantage API, and StockData instance
        String apiKey = "G89M0HECMYPKA46T";
        int timeout = 3000;
        AlphaVantageConnector connector = new AlphaVantageConnector(apiKey, timeout);
        StockData stockData = new StockData(connector);

        // all data requests are called by AVRequests
        AVRequest request = new AVRequest();

        // sample request to pull test stock
        //request.testRequest(stockData);

        // pull tech sector
        request.techSectorRequest(stockData);
    }
}

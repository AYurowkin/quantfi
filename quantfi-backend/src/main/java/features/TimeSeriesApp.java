package features;

import connection.AlphaVantageConnector;
import connection.AlphaVantageException;
import data.*;

import java.util.List;
import java.util.Map;

public class TimeSeriesApp {
    public static void main(String[] args) {
        String apiKey = "G89M0HECMYPKA46T";
        int timeout = 3000;
        AlphaVantageConnector connector = new AlphaVantageConnector(apiKey, timeout);
        StockData timeSeries = new StockData(connector);

        try {
            IntraDay response = timeSeries.intraDay("MSFT", Interval.ONE_MIN, OutputSize.COMPACT);
            Map<String, String> metaData = response.getMetaData();
            System.out.println("Information: " + metaData.get("1. Information"));
            System.out.println("Stock: " + metaData.get("2. Symbol"));

            List<StockInfo> stockInfoList = response.getStockInfoList();
            stockInfoList.forEach(stock -> {
                System.out.println("date: " + stock.getLocalDateTime());
                System.out.println("open: " + stock.getOpen());
                System.out.println("high: " + stock.getHigh());
                System.out.println("low: " + stock.getLow());
                System.out.println("close: " + stock.getClose());
                System.out.println("volume: " + stock.getVolume());
            });
        } catch (AlphaVantageException e) {
            System.out.println("failed to print stock data");
        }
    }
}

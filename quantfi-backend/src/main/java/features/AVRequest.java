package features;

import connection.AlphaVantageException;
import data.*;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;

// class to create requests to Alpha Vantage API
class AVRequest {

    void testRequest(StockData stockData) {
        try {
            IntraDay response = stockData.intraDay("WUBA", Interval.ONE_MIN, OutputSize.COMPACT);
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
            throw new AlphaVantageException("failed to print stock data", e);
        }
    }

    void techSectorRequest(StockData stockData) {
        try {
            String filepath = "quantfi-backend/data-storage/preprocessed/companylist.csv";
            Reader reader = Files.newBufferedReader(Paths.get(filepath));
            CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT
            .withHeader("Symbol", "Name", "MarketCap", "ADR TSO", "IPOyear", "Sector", "Industry", "Summary Quote")
            .withIgnoreHeaderCase()
            .withTrim());

            //parse csv and get list of stocks in tech sector
            ArrayList<String> techSectorList = new ArrayList<>();
            for (CSVRecord csvRecord : csvParser) {
                techSectorList.add(csvRecord.get("Symbol"));
            }
            techSectorList.remove(0);   //removes column name Symbol
            int count = 0;
            for (String stock : techSectorList) {
                //requests latest 100 data points of daily information of each tech sector stock
                stockData.daily(stock, OutputSize.FULL);
                //TODO: trim the json output based on date
                count++;
                if (count == 4) {
                    count = 0;
                    TimeUnit.MINUTES.sleep(1);
                }
                //TODO: figure out how to pay for the Alpha Vantage premium version
            }
        } catch (Exception e) {
            throw new AlphaVantageException("failed to retrieve tech sector stocks", e);
        }
    }
}

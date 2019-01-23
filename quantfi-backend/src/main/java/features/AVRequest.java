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

    void testRequest(StockData stock_data) {
        try {
            Daily response = stock_data.daily("MSFT", OutputSize.FULL);
            Map<String, String> meta_data = response.getMetaData();
            String stock_symbol = meta_data.get("2. Symbol");

            List<StockInfo> stock_info_list = response.getStockInfoList();
            //convert stock_info_list into a csv file (both full and trimmed)
            Conversion conversion = new Conversion();
            conversion.dailyConversion(stock_info_list, stock_symbol);
            conversion.dailyConversionTrim(stock_info_list, stock_symbol);
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
                //print stock name
                System.out.println(stock);
                //requests latest 100 data points of daily information of each tech sector stock
                Daily response = stockData.daily(stock, OutputSize.FULL);
                //convert to csv file and store
                List<StockInfo> stock_info_list = response.getStockInfoList();
                Conversion conversion = new Conversion();
                conversion.dailyConversion(stock_info_list, stock);
                conversion.dailyConversionTrim(stock_info_list, stock);
                count++;
                if (count == 4) {
                    count = 0;
                    TimeUnit.MINUTES.sleep(2);
                }
            }
        } catch (Exception e) {
            throw new AlphaVantageException("failed to retrieve tech sector stocks", e);
        }
    }
}

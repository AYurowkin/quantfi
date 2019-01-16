package data;

import com.opencsv.CSVWriter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Conversion {

    //converts JSON files from tech_daily_last_100 into csv format
    public void techDailyConversion(List<StockInfo> stock_info_list, String stock_symbol) {
        //create new csv file for tech daily stock
        File file = new File("quantfi-backend/data-storage/test_stocks/" + stock_symbol + "_Daily.csv");
        try {
            FileWriter output_file = new FileWriter(file);
            CSVWriter writer = new CSVWriter(output_file);
            //create header for tech stock
            String[] header = {"Date", "Open", "High", "Low", "Close", "Volume"};
            writer.writeNext(header);
            stock_info_list.forEach(stock -> {
                //generate new line for each day and populate with appropriate values
                //TODO: need to remove timestamp from LocalDateTime. Example: 2019-01-15T00:00
                String[] data = {stock.getLocalDateTime().toLocalDate().toString(), String.valueOf(stock.getOpen()),
                        String.valueOf(stock.getHigh()), String.valueOf(stock.getLow()),
                        String.valueOf(stock.getClose()), String.valueOf(stock.getVolume())};
                writer.writeNext(data);
            });
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}

package data;

import com.opencsv.CSVWriter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Conversion {

    //converts JSON files from tech_daily_last_100 into csv format
    public void dailyConversion(List<StockInfo> stock_info_list, String stock_symbol) {
        //create new csv file in daily_csv folder for daily stock quote
        File file = new File("quantfi-backend/data-storage/daily_csv/" + stock_symbol + "_Daily.csv");
        try {
            FileWriter output_file = new FileWriter(file);
            CSVWriter writer = new CSVWriter(output_file);
            //create header for tech stock
            String[] header = {"Date", "Open", "High", "Low", "Close", "Volume"};
            writer.writeNext(header);
            stock_info_list.forEach(stock -> {
                //generate new line for each day and populate with appropriate values
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

    //converts JSON files from tech_daily_last_100 into a trimmed csv format (Years 2012 - 2018) for NN training
    public void dailyConversionTrim(List<StockInfo> stock_info_list, String stock_symbol) {
        File file = new File("quantfi-backend/data-storage/daily_csv_trim/" + stock_symbol + "_Daily.csv");
        try {
            FileWriter output_file = new FileWriter(file);
            CSVWriter writer = new CSVWriter(output_file);
            String[] header = {"Date", "Open", "High", "Low", "Close", "Volume"};
            writer.writeNext(header);
            stock_info_list.forEach(stock -> {
                //only proceed to generate new line if date is after year 2012 and before 2018 (inclusive)
                if (stock.getLocalDateTime().getYear() >= 2012 && stock.getLocalDateTime().getYear() <= 2018) {
                    //generate new line for each day and populate with appropriate values
                    String[] data = {stock.getLocalDateTime().toLocalDate().toString(), String.valueOf(stock.getOpen()),
                            String.valueOf(stock.getHigh()), String.valueOf(stock.getLow()),
                            String.valueOf(stock.getClose()), String.valueOf(stock.getVolume())};
                    writer.writeNext(data);
                }
            });
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

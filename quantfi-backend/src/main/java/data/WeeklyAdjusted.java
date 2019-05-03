package data;

import connection.AlphaVantageException;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class WeeklyAdjusted extends StockDataResponse {

    private WeeklyAdjusted(final Map<String, String> metaData, final List<StockInfo> stockInfoList) {
        super(metaData, stockInfoList);
    }

    public static WeeklyAdjusted from(String json) {
        return null;
    }

    // parses the stock and retrieves prices with the weekly adjusted timestamp
    private static class Parser extends StockDataParser<WeeklyAdjusted> {

        @Override
        String getStockDataKey() {
            return "Weekly Adjusted Time Series";
        }

        @Override
        WeeklyAdjusted resolve(Map<String, String> metaData, Map<String, Map<String, String>> stockData) {
            List<StockInfo> stocks = new ArrayList<>();

            try {
                stockData.forEach((key, values) -> stocks.add(new StockInfo(
                        LocalDate.parse(key, DATE_SIMPLE_FORMAT).atStartOfDay(),
                        Double.parseDouble(values.get("1. open")),
                        Double.parseDouble(values.get("2. high")),
                        Double.parseDouble(values.get("3. low")),
                        Double.parseDouble(values.get("4. close")),
                        Double.parseDouble(values.get("5. adjusted close")),
                        Long.parseLong(values.get("6. volume")),
                        Double.parseDouble(values.get("7. dividend amount"))
                )));
            } catch (Exception e) {
                throw new AlphaVantageException("API Weekly Adjusted Stock Info error");
            }

            return new WeeklyAdjusted(metaData, stocks);
        }
    }
}

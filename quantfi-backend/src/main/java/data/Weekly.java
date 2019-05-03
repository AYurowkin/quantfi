package data;

import connection.AlphaVantageException;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Weekly extends StockDataResponse {

    private Weekly(final Map<String, String> metaData, final List<StockInfo> stockInfoList) {
        super(metaData, stockInfoList);
    }

    public static Weekly from(String json) {
        Parser parser = new Parser();
        return parser.parseJson(json);
    }

    // parses the stock and retrieves prices with the weekly timestamp
    public static class Parser extends StockDataParser<Weekly> {

        @Override
        String getStockDataKey() {
            return "Weekly Time Series";
        }

        @Override
        Weekly resolve(Map<String, String> metadata, Map<String, Map<String, String>> stockData) {
            List<StockInfo> stocks = new ArrayList<>();

            try {
                stockData.forEach((key, values) -> stocks.add(new StockInfo(
                        LocalDate.parse(key, DATE_SIMPLE_FORMAT).atStartOfDay(),
                        Double.parseDouble(values.get("1. open")),
                        Double.parseDouble(values.get("2. high")),
                        Double.parseDouble(values.get("3. low")),
                        Double.parseDouble(values.get("4. close")),
                        Long.parseLong(values.get("5. volume"))
                )));
            } catch (Exception e) {
                throw new AlphaVantageException("API Weekly Stock Info error");
            }

            return new Weekly(metadata, stocks);
        }
    }
}

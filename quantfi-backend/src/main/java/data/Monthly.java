package data;

import connection.AlphaVantageException;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Monthly extends StockDataResponse {

    private Monthly(final Map<String, String> metaData, final List<StockInfo> stockInfoList) {
        super(metaData, stockInfoList);
    }

    public static Monthly from(String json) {
        Parser parser = new Parser();
        return parser.parseJson(json);
    }

    // parses the stock and retrieves prices with the monthly timestamp
    public static class Parser extends StockDataParser<Monthly> {

        @Override
        String getStockDataKey() {
            return "Monthly Time Series";
        }

        @Override
        Monthly resolve(Map<String, String> metaData, Map<String, Map<String, String>> stockData) {
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
                throw new AlphaVantageException("API Monthly Stock Info error", e);
            }

            return new Monthly(metaData, stocks);
        }
    }
}

package data;

import connection.AlphaVantageException;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
public class MonthlyAdjusted extends StockDataResponse {

    private MonthlyAdjusted(final Map<String, String> metaData, final List<StockInfo> stockInfoList) {
        super(metaData, stockInfoList);
    }

    public static MonthlyAdjusted from(String json) {
        Parser parser = new Parser();
        return parser.parseJson(json);
    }

    private static class Parser extends StockDataParser<MonthlyAdjusted> {

        @Override
        String getStockDataKey() {
            return "Monthly Adjusted Time Series";
        }

        @Override
        MonthlyAdjusted resolve(Map<String, String> metaData, Map<String, Map<String, String>> stockData) {
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
                throw new AlphaVantageException("API Monthly Adjusted Stock Info error");
            }

            return new MonthlyAdjusted(metaData, stocks);
        }
    }
}

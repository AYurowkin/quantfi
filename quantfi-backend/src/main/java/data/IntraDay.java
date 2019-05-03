package data;

import connection.AlphaVantageException;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class IntraDay extends StockDataResponse {

    private IntraDay(final Map<String, String> metaData, final List<StockInfo> stockInfoList) {
        super(metaData, stockInfoList);
    }

    public static IntraDay from(Interval interval, String json) {
        IntraDay.Parser parser = new IntraDay.Parser(interval);
        return parser.parseJson(json);
    }

    // parses the stock and retrieves prices with the intraday timestamp
    private static class Parser extends StockDataParser<IntraDay> {
        private final Interval interval;

        Parser(Interval interval) {
            this.interval = interval;
        }

        @Override
        String getStockDataKey() {
            return "Time Series (" + interval.getValue() + ")";
        }

        @Override
        IntraDay resolve(Map<String, String> metaData, Map<String, Map<String, String>> stockData) {
            List<StockInfo> stocks = new ArrayList<>();
            try {
                stockData.forEach((key, values) -> stocks.add(new StockInfo(
                        LocalDateTime.parse(key, DATE_WITH_TIME_FORMAT),
                        Double.parseDouble(values.get("1. open")),
                        Double.parseDouble(values.get("2. high")),
                        Double.parseDouble(values.get("3. low")),
                        Double.parseDouble(values.get("4. close")),
                        Long.parseLong(values.get("5. volume"))
                )));
            } catch (Exception e) {
                throw new AlphaVantageException("API IntraDay StockInfo error");
            }
            return new IntraDay(metaData, stocks);
        }
    }
}

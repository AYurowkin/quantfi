package data;

import java.util.List;
import java.util.Map;

// template for the response of each time period.

public class StockDataResponse {

    private final Map<String, String> metaData;
    private final List<StockInfo> stockInfoList;

    StockDataResponse(final Map<String, String> metaData, final List<StockInfo> stockInfoList) {
        this.metaData = metaData;
        this.stockInfoList = stockInfoList;
    }

    public Map<String, String> getMetaData() {
        return metaData;
    }

    public List<StockInfo> getStockInfoList() {
        return stockInfoList;
    }
}

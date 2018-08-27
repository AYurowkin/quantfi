package data;

import java.util.List;
import java.util.Map;

public class Daily extends StockDataResponse {

    private Daily(final Map<String, String> metaData,final List<StockInfo> stockInfoList) {
        super(metaData, stockInfoList);
    }

//    public static Daily from(String json) {
//        Parser parser = new Parser();
//        return parser.parseJson(json);
//    }

}

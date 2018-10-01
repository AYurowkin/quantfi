package data;

import com.google.gson.JsonObject;
import com.google.gson.JsonSyntaxException;
import com.google.gson.reflect.TypeToken;
import connection.AlphaVantageException;

import java.io.FileWriter;
import java.lang.reflect.Type;
import java.util.Map;

public abstract class StockDataParser<Data> extends JsonParser<Data> {

    abstract Data resolve(Map<String, String> metadata, Map<String, Map<String, String>> stockData);

    abstract String getStockDataKey();

    @Override
    public Data resolve(JsonObject jsonObject) {
        Type metaDataType = new TypeToken<Map<String, String>>(){}.getType();
        Type stockDataType = new TypeToken<Map<String, Map<String, String>>>(){}.getType();

        try {
            Map<String, String> metaData = GSON.fromJson(jsonObject.get("Meta Data"), metaDataType);
            Map<String, Map<String, String>> stockData = GSON.fromJson(jsonObject.get(getStockDataKey()), stockDataType);
            storeData(jsonObject);
            return resolve(metaData, stockData);
        } catch (JsonSyntaxException e) {
            throw new AlphaVantageException("API data change", e);
        }
    }

    private void storeData(JsonObject jsonObject) {
        try {
            FileWriter fw = new FileWriter("quantfi-backend/data-storage/data.txt");
            fw.write(jsonObject.toString());
            fw.close();
        } catch (Exception e) {
            throw new AlphaVantageException("Failure to write JSON object to text file.");
        }
    }
}

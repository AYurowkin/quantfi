package data;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonSyntaxException;
import connection.AlphaVantageException;

import java.time.format.DateTimeFormatter;

public abstract class JsonParser<Data> {

    protected final DateTimeFormatter DATE_SIMPLE_FORMAT = DateTimeFormatter.ofPattern("yyyy-MM-dd");
    protected final DateTimeFormatter DATE_WITH_TIME_FORMAT = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    protected final DateTimeFormatter DATE_WITH_SIMPLE_TIME_FORMAT = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

    private static com.google.gson.JsonParser JSON_PARSER = new com.google.gson.JsonParser();

    protected static Gson GSON = new Gson();

    protected abstract Data resolve(JsonObject jsonObject);

    public Data parseJson(String json) {
        try {
            JsonElement jsonElement = JSON_PARSER.parse(json);
            JsonObject jsonObject = jsonElement.getAsJsonObject();
            JsonElement errorMessage = jsonObject.get("Error Message");

            if (errorMessage != null) {
                throw new AlphaVantageException(errorMessage.getAsString());
            }
            return resolve(jsonObject);
        } catch (JsonSyntaxException e) {
            throw new AlphaVantageException("json parsing error", e);
        }
    }
}
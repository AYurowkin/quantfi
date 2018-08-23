import com.sun.istack.internal.Nullable;

public class ApiParameterBuilder {
    private StringBuilder urlBuilder;

    public ApiParameterBuilder() {
        this.urlBuilder = new StringBuilder();
    }

    public void append(@Nullable ApiParameter apiParameter) {
        if (apiParameter != null) {
            append(apiParameter.getKey(), apiParameter.getValue());
        }
    }

    public void append(String key, String value) {
        String parameter = "&" + key + "=" + value;
        this.urlBuilder.append(parameter);
    }

    public String getUrl() {
        return this.urlBuilder.toString();
    }
}
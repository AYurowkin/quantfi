package connection;

import com.sun.istack.internal.Nullable;

public class ApiParameterBuilder {
    private StringBuilder urlBuilder;

    public ApiParameterBuilder() {
        this.urlBuilder = new StringBuilder();
    }

    // append parameter to URL
    public void append(@Nullable ApiParameter apiParameter) {
        if (apiParameter != null) {
            append(apiParameter.getKey(), apiParameter.getValue());
        }
    }

    // appaends key and value to the URL
    public void append(String key, String value) {
        String parameter = "&" + key + "=" + value;
        this.urlBuilder.append(parameter);
    }

    // returns built URL
    public String getUrl() {
        return this.urlBuilder.toString();
    }
}
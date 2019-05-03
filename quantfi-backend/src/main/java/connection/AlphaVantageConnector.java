package connection;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class AlphaVantageConnector implements ApiConnector {

    private static final String URL = "https://www.alphavantage.co/query?";
    // apiKey to access Alpha Vantage API
    private final String apiKey;
    // count when the connection should be timed out
    private final int connectionTimeOut;

    public AlphaVantageConnector(String apiKey, int connectionTimeOut) {
        this.apiKey = apiKey;
        this.connectionTimeOut = connectionTimeOut;
    }

    // Main method to pass in URL and connect to Alpha Vantage API
    @Override
    public String getRequest(ApiParameter... apiParameters) {
        String parameters = getParameters(apiParameters);
        try {
            URL request = new URL(URL + parameters);
            URLConnection connection = request.openConnection();
            connection.setConnectTimeout(connectionTimeOut);
            connection.setReadTimeout(connectionTimeOut);

            InputStreamReader inputStreamReader = new InputStreamReader(connection.getInputStream(), "UTF-8");
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            StringBuilder responseBuilder = new StringBuilder();

            String currentLine;
            while ((currentLine = bufferedReader.readLine()) != null) {
                responseBuilder.append(currentLine);
            }
            bufferedReader.close();
            return responseBuilder.toString();
        } catch (IOException e) {
            throw new AlphaVantageException("Failed to send request.", e);
        }
    }

    // Add parameters to the URL
    private String getParameters(ApiParameter... apiParameters) {
        ApiParameterBuilder urlBuilder = new ApiParameterBuilder();
        for (ApiParameter apiParameter : apiParameters) {
            urlBuilder.append(apiParameter);
        }
        urlBuilder.append("apikey", apiKey);
        return urlBuilder.getUrl();
    }


}
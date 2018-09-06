package data;

import connection.ApiParameter;

public enum Function implements ApiParameter {

    TIME_SERIES_INTRADAY("TIME_SERIES_INTRADAY"),
    TIME_SERIES_DAILY("TIME_SERIES_DAILY"),
    TIME_SERIES_DAILY_ADJUSTED("TIME_SERIES_DAILY_ADJUSTED"),
    TIME_SERIES_WEEKLY("TIME_SERIES_WEEKLY"),
    TIME_SERIES_WEEKLY_ADJUSTED("TIME_SERIES_WEEKLY_ADJUSTED"),
    TIME_SERIES_MONTHLY("TIME_SERIES_MONTHLY"),
    TIME_SERIES_MONTHLY_ADJUSTED("TIME_SERIES_MONTHLY_ADJUSTED");

    private final String urlParameter;

    Function(String urlParameter) {
        this.urlParameter = urlParameter;
    }

    @Override
    public String getKey() {
        return "function";
    }

    @Override
    public String getValue() {
        return urlParameter;
    }
}

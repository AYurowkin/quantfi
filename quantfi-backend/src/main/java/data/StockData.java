package data;

import connection.ApiConnector;

// main class with time series functions to pull in historical data of a given stock.

public class StockData {
    private final ApiConnector connector;

    public StockData(ApiConnector connector) {
        this.connector = connector;
    }

    public IntraDay intraDay(String symbol, Interval interval, OutputSize outputSize) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_INTRADAY, interval, outputSize);
        return IntraDay.from(interval, json);
    }

    public IntraDay intraDay(String symbol, Interval interval) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_INTRADAY, interval);
        return IntraDay.from(interval, json);
    }

    public Daily daily(String symbol, OutputSize outputSize) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_DAILY, outputSize);
        return Daily.from(json);
    }

    public Daily daily(String symbol) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_DAILY);
            return Daily.from(json);
    }

    public DailyAdjusted dailyAdjusted(String symbol, OutputSize outputSize) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_DAILY_ADJUSTED, outputSize);
        return DailyAdjusted.from(json);
    }

    public Weekly weekly(String symbol) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_WEEKLY);
        return Weekly.from(json);
    }

    public WeeklyAdjusted weeklyAdjusted(String symbol) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_WEEKLY_ADJUSTED);
        return WeeklyAdjusted.from(json);
    }

    public Monthly monthly(String symbol) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_MONTHLY);
        return Monthly.from(json);
    }

    public MonthlyAdjusted monthlyAdjusted(String symbol) {
        String json = connector.getRequest(new Symbol(symbol), Function.TIME_SERIES_MONTHLY_ADJUSTED);
        return MonthlyAdjusted.from(json);
    }
}

package data;

import java.time.LocalDateTime;

// base class that holds all information about a given stock.

public class StockInfo {
    private final LocalDateTime localDateTime;
    private final double open;
    private final double high;
    private final double low;
    private final double close;
    private final double adjustedClose;
    private final long volume;
    private final double dividendAmount;
    private final double splitCoefficient;

    public StockInfo(LocalDateTime localDateTime,
                     double open,
                     double high,
                     double low,
                     double close,
                     double adjustedClose,
                     long volume,
                     double dividendAmount,
                     double splitCoefficient) {
        this.localDateTime = localDateTime;
        this.open = open;
        this.high = high;
        this.low = low;
        this.close = close;
        this.adjustedClose = adjustedClose;
        this.volume = volume;
        this.dividendAmount = dividendAmount;
        this.splitCoefficient = splitCoefficient;
    }

    public StockInfo(LocalDateTime localDateTime,
                     double open,
                     double high,
                     double low,
                     double close,
                     double adjustedClose,
                     long volume,
                     double dividendAmount) {
        this.localDateTime = localDateTime;
        this.open = open;
        this.high = high;
        this.low = low;
        this.close = close;
        this.adjustedClose = adjustedClose;
        this.volume = volume;
        this.dividendAmount = dividendAmount;
        this.splitCoefficient = 0.0;
    }

    public StockInfo(LocalDateTime localDateTime,
                     double open,
                     double high,
                     double low,
                     double close,
                     long volume) {
        this.localDateTime = localDateTime;
        this.open = open;
        this.high = high;
        this.low = low;
        this.close = close;
        this.adjustedClose = 0.0;
        this.volume = volume;
        this.dividendAmount = 0.0;
        this.splitCoefficient = 0.0;
    }

    public LocalDateTime getLocalDateTime() {
        return localDateTime;
    }

    public double getOpen() {
        return open;
    }

    public double getHigh() {
        return high;
    }

    public double getLow() {
        return low;
    }

    public double getClose() {
        return close;
    }

    public double getAdjustedClose() {
        return adjustedClose;
    }

    public long getVolume() {
        return volume;
    }

    public double getDividendAmount() {
        return dividendAmount;
    }

    public double getSplitCoefficient() {
        return splitCoefficient;
    }
}

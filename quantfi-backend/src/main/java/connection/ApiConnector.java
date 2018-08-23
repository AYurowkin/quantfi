package connection;

@FunctionalInterface
public interface ApiConnector {
    String getRequest(ApiParameter... parameter);
}

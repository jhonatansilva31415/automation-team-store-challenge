def test_echo(test_app, test_database):
    """
    Given a dev wants to start out developing this API
    When he asks for an echo endpoint
    Then the system must return a simple echo message
    """
    client = test_app.test_client()
    response = client.get("/test/echo")
    data = response.json
    assert data == {"echo": "echo"}

from perfsize.perfsize import Hello


class TestHello:
    def test_hello(self) -> None:
        hello = Hello()
        assert hello.greet("World") == "Hello World"

module:
	if ! test -f target/jolokia-agent.jar; then mvn package -q -DskipTests=true; fi

clean:
	mvn clean
	-rm -f dependency-reduced-pom.xml

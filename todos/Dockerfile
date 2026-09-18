FROM docker.io/library/eclipse-temurin:17.0.13_11-jre-jammy

USER 1001
WORKDIR /app

COPY --chown=1001:0 target/todos.jar todos.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app/todos.jar"]

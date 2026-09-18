package de.ordix.devops.todos.config;

import de.ordix.devops.todos.model.Priority;
import de.ordix.devops.todos.model.Todo;
import de.ordix.devops.todos.repository.TodosRepository;
import java.time.LocalDateTime;
import java.util.List;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Command Line runner
 *
 * @author ngj
 */
@Configuration
public class TodosConfig {

    @Bean
    public CommandLineRunner commandLineRunner(TodosRepository repository) {
	return args -> {
	    List<Todo> todos
		    = List.of(
			    Todo.builder()
				    .title("Java Microservice Impl.")
				    .createdAt(LocalDateTime.now())
				    .priority(Priority.NORMAL)
				    .isDone(false)
				    .build(),
			    Todo.builder()
				    .title("Dockerize Appl.")
				    .createdAt(LocalDateTime.now())
				    .priority(Priority.NORMAL)
				    .isDone(false)
				    .build(),
			    Todo.builder()
				    .title("deploy on k8s Cluster using k8s Manifests files")
				    .createdAt(LocalDateTime.now())
				    .priority(Priority.NORMAL)
				    .isDone(false)
				    .build(),
			    Todo.builder()
				    .title("Refactor K8s Manifest to Helm Chart")
				    .createdAt(LocalDateTime.now())
				    .priority(Priority.NORMAL)
				    .isDone(false)
				    .build()
		    );
	    repository.saveAll(todos);

	};
    }

}

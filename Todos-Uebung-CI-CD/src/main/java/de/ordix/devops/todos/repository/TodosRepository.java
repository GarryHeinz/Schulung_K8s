package de.ordix.devops.todos.repository;

import de.ordix.devops.todos.model.Todo;
import java.util.UUID;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * JPA Repo
 * @author ngj
 */
@Repository
public interface TodosRepository 
	extends JpaRepository<Todo, UUID>{
    
}

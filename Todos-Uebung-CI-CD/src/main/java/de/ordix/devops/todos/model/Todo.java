package de.ordix.devops.todos.model;

import jakarta.persistence.Column;
import jakarta.persistence.Convert;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import java.time.LocalDateTime;
import java.util.UUID;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Model Entity
 * @author ngj
 */
@Entity
@Table
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Todo {
    
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    private String title;
    @Column(name = "CREATION_DATE")
    private LocalDateTime createdAt;
    @Convert(converter = PriorityAttributeConverter.class)
    private Priority priority;
    @Column(name = "STATUS")
    private boolean isDone;
    
}

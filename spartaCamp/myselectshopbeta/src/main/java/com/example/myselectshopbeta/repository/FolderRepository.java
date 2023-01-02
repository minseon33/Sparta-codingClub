package com.example.myselectshopbeta.repository;


import com.example.myselectshopbeta.entity.Folder;
import com.example.myselectshopbeta.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface FolderRepository extends JpaRepository<Folder, Long> {

    List<Folder> findAllByUser(User user);
    List<Folder> findAllByUserAndNameIn(User user, List<String> names);

}
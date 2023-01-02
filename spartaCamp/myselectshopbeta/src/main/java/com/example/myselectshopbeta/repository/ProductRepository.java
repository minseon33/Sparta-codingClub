package com.example.myselectshopbeta.repository;

import com.example.myselectshopbeta.dto.ProductMypriceRequestDto;
import com.example.myselectshopbeta.dto.ProductResponseDto;
import com.example.myselectshopbeta.entity.Product;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

public interface ProductRepository extends JpaRepository<Product, Long> {
    Page<Product> findAllByUserId(Long userId, Pageable pageable);
    Optional<Product> findByIdAndUserId(Long id, Long userId);
    Page<Product> findAll(Pageable pageable);
    Page<Product> findAllByUserIdAndFolderList_Id(Long userId, Long folderId, Pageable pageable);
    Optional<Product> findByIdAndFolderList_Id(Long productId, Long folderId);
}
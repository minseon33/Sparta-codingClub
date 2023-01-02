//package com.example.myselectshopbeta.config;
//
//
//import com.example.myselectshopbeta.repository.ProductRepository;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//
//@Configuration
//public class BeanConfiguration {
//    @Bean
//    public ProductRepository productRepository() {
//        String dbUrl = "jdbc:h2:mem:db";
//        String username = "sa";
//        String password = "";
//        ProductRepository productRepository = new ProductRepository(dbUrl, username, password);
//        return productRepository;
//
//    }
//}
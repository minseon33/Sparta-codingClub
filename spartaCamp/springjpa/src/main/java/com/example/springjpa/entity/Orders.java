package com.example.springjpa.entity;


import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Getter
@Entity
@NoArgsConstructor
public class Orders {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private  Long id;

    @ManyToOne
    @JoinColumn(name = "food_id") //food 아이디와 조인된다는 어노테이션
    private Food food;

    @ManyToOne
    @JoinColumn(name = "member_id")
    private Member member;

    public Orders(Food food, Member member) {
        this.food = food;
        this.member = member;
    }



}

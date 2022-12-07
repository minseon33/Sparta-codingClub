package com.example.springjpa.entity;


import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Getter // 데이터값 가져오는 게터 쓸 수 있게 해주는 어노테이션
@Entity // 엔터티라고 알려주는 어노테이션
@NoArgsConstructor //기본생성자 만들어주는 어노테이션
public class Member {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String memberName;

    @OneToMany(mappedBy = "member" , fetch = FetchType.EAGER)
    private List<Orders> orders = new ArrayList<>();

    public Member(String memberName) {
        this.memberName = memberName;
    }
}

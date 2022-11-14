package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(Long id); // Optional , null 처리 방법중 하나, (구글링 해보기)
    Optional<Member> findByName(String name);
    List<Member> findAll();
}

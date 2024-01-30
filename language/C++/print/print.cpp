// input output 을 관리하는 헤더
// 확장자는 .h 지만 C++ 에서는 표준 헤더파일에는 확장자를 붙이지 않는다.
#include <iostream>

int main()
{
    // 출력
    // std 의 cout 이 출력 명령어
    // << 의 뒤에는 정수 실수 문자열 변수 등 무엇이든 올 수 있다.
    // %d %s 같은 서실문자를 이용해 포맷을 지정하지 않아도 적절하게 출력된다.
    // << 도 연산자이며 << "hello" << "world" 와 같이 연달아 사용할수 있다. > "helloworld"
    // std::endl; 은 개행으로 이어진다.
    std::cout << "Hello World" << std::endl;

    // 입력
    // std 의 cin 이 입력 명령어
    // >> 으로 입력 문자를 할당한다.
    // 변수의 선언은 어느 위치에서도 가능하다.
    // cin >> val1 >> val2 와 같이 명령하면 첫번째 입력과 두번째 입력을 연속해서 받을수 있으며
    // 이 입력들은 공백으로 구분한다.
    int val1;
    std::cout << "첫 번째 입력: ";
    std::cin >> val1;

    int val2;
    std::cout << "두 번째 입력: ";
    std::cin >> val2;

    int result = val1 + val2;
    std::cout << "덧셈 결과: " << result << std::endl;

    // 문자열 입출력
    char name[100];
    char lang[200];
    std::cout << "이름이 무엇입니까? : ";
    std::cin >> name;
    std::cout << "어떤 프로그래밍 언어를 사용하십니까? : ";
    std::cin >> lang;
    // \n 과 endl 은 모두 엔터키로 작동하며 큰 차이가 없지만 endl 은 출력 버퍼를 플러시한다.
    // 버퍼 플러시는 데이터를 임시 저장소에서 영구적인 데이터 저장소로 전송하는 것을 말한다.
    // 많은 데이터를 출력하며 속도를 빠르게 하고 싶다면 \n 을, 프로그램이 불안정한 경우 endl 을 사용한다.
    std::cout << "제 이름은 " << name << "입니다.\n";
    std::cout << "사용하는 프로그래밍 언어는 " << lang << "입니다." << std::endl;

    return 0;
}
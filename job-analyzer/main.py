import re


# 현재 내가 가지고 있는 기술
MY_SKILLS = [
    "Python",
    "SQL",
    "Git",
    "Linux",
]


# 분석할 수 있는 기술 목록
SKILLS = [
    "Python",
    "SQL",
    "FastAPI",
    "Docker",
    "Git",
    "Linux",
    "AWS",
    "Azure",
    "Java",
    "JavaScript",
    "React",
    "PyTorch",
    "TensorFlow",
]


def extract_skills(text):
    """채용공고에서 기술 스택을 추출한다."""
    found_skills = []

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


def analyze_gap(required_skills):
    """채용공고의 요구 기술과 내 기술을 비교한다."""
    my_skills_lower = [skill.lower() for skill in MY_SKILLS]

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in my_skills_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing


def recommend_learning(missing_skills):
    """부족한 기술에 대한 학습 키워드를 추천한다."""
    recommendations = {
        "FastAPI": "FastAPI CRUD 및 REST API 개발",
        "Docker": "Dockerfile 및 Docker Compose",
        "AWS": "AWS EC2와 기본 배포",
        "Azure": "Azure 기본 서비스와 배포",
        "Java": "Java 객체지향 프로그래밍",
        "JavaScript": "JavaScript 기본 문법 및 비동기 처리",
        "React": "React 컴포넌트와 상태 관리",
        "PyTorch": "PyTorch 딥러닝 기초",
        "TensorFlow": "TensorFlow 모델 구축 기초",
    }

    return [
        recommendations[skill]
        for skill in missing_skills
        if skill in recommendations
    ]


def analyze_job_description(job_description):
    """채용공고 전체를 분석한다."""

    required_skills = extract_skills(job_description)

    matched, missing = analyze_gap(required_skills)

    recommendations = recommend_learning(missing)

    return required_skills, matched, missing, recommendations


def print_result(required_skills, matched, missing, recommendations):
    """분석 결과를 보기 좋게 출력한다."""

    print("\n" + "=" * 50)
    print("                 분석 결과")
    print("=" * 50)

    print("\n[1. 채용공고 요구 기술]")

    if required_skills:
        for skill in required_skills:
            print(f"- {skill}")
    else:
        print("- 발견된 기술이 없습니다.")

    print("\n[2. 내가 보유한 기술]")

    if matched:
        for skill in matched:
            print(f"- {skill}")
    else:
        print("- 일치하는 기술이 없습니다.")

    print("\n[3. 부족한 기술]")

    if missing:
        for skill in missing:
            print(f"- {skill}")
    else:
        print("- 부족한 기술이 없습니다.")

    print("\n[4. 추천 학습]")

    if recommendations:
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("- 추가 학습 추천이 없습니다.")

    print("\n" + "=" * 50)


def main():
    print("=" * 50)
    print("          AI Job Description Analyzer")
    print("=" * 50)

    print("\n채용공고를 붙여넣어 주세요.")
    print("입력을 끝내려면 마지막 줄에서 Ctrl+D를 누르세요.")
    print("-" * 50)

    lines = []

    try:
        while True:
            line = input()
            lines.append(line)

    except EOFError:
        pass

    job_description = "\n".join(lines)

    if not job_description.strip():
        print("\n채용공고가 입력되지 않았습니다.")
        return

    required_skills, matched, missing, recommendations = (
        analyze_job_description(job_description)
    )

    print_result(
        required_skills,
        matched,
        missing,
        recommendations,
    )


if __name__ == "__main__":
    main()
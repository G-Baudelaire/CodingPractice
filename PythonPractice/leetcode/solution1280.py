import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how="cross")
    df2 = examinations.value_counts().reset_index()
    df = df.merge(df2, how="left", on=["student_id", "subject_name"]).rename(columns={"count": "attended_exams"})
    df["attended_exams"] = df["attended_exams"].fillna(0)
    df = df.sort_values(["student_id", "subject_name"], ascending=[True, True])
    return df
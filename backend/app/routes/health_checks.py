from flask import Flask, Blueprint, render_template

health_checks_bp = Blueprint("health_checks", __name__)

@health_checks_bp.get("/health_check")
def health_check():
    return("TA FUNFANDO")
{% extends 'base.html' %}
{% load static %}
{% block title %}Gas Blending{% endblock %}
{% block content %}

<form method="post" action="{% url 'gasblending:gas_blending' %}">
  {% csrf_token %}
  <div class="form-group">
    <h2>Input Gas Percentages</h2>
    <label for="current_o2">Current Oxygen Percentage:</label>
    <input type="number" class="form-control" id="current_o2" name="current_o2" min="0" max="100" step="0.01" value="{{ current_o2 }}" required>
    <p class="default-settings">Default: 21%</p>
  </div>
  <div class="form-group">
    <label for="current_n2">Current Nitrogen Percentage:</label>
    <input type="number" class="form-control" id="current_n2" name="current_n2" min="0" max="100" step="0.01" value="{{ current_n2 }}" required>
    <p class="default-settings">Default: 78%</p>
  </div>
  <div class="form-group">
    <h2>Input Gas to Add (in PSI)</h2>
    <label for="oxygen">Oxygen:</label>
    <input type="number" class="form-control" id="oxygen" name="oxygen.

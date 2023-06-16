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
    <input type="number" class="form-control" id="oxygen" name="oxygen" min="0" step="1" value="{{ oxygen }}" required>
  </div>
  <div class="form-group">
    <label for="nitrogen">Nitrogen:</label>
    <input type="number" class="form-control" id="nitrogen" name="nitrogen" min="0" step="1" value="{{ nitrogen }}" required>
  </div>
  <div class="form-group">
    <label for="helium">Helium:</label>
    <input type="number" class="form-control" id="helium" name="helium" min="0" step="1" value="{{ helium }}" required>
  </div>
  <div class="form-group">
    <h2>Target Partial Pressure of Oxygen (in PSI)</h2>
    <label for="target_ppo2">Target pO2:</label>
    <input type="number" class="form-control" id="target_ppo2" name="target_ppo2" min="0" step="0.01" value="{{ target_ppo2 }}" required>
  </div>
  <button type="submit" class="btn btn-primary">Calculate</button>
</form>

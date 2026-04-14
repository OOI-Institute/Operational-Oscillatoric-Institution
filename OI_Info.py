
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font-sans); }
.section { margin-bottom: 2rem; }
.section-label { font-size: 11px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: var(--color-text-tertiary); margin-bottom: 0.75rem; }
.card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem 1.25rem; }
.pill { display: inline-block; font-size: 11px; font-weight: 500; padding: 2px 8px; border-radius: 99px; }
.pill-purple { background: #EEEDFE; color: #3C3489; }
.pill-teal { background: #E1F5EE; color: #085041; }
.pill-amber { background: #FAEEDA; color: #633806; }
.pill-coral { background: #FAECE7; color: #4A1B0C; }
.pill-blue { background: #E6F1FB; color: #0C447C; }
.pill-gray { background: #F1EFE8; color: #444441; }
@media (prefers-color-scheme: dark) {
  .pill-purple { background: #26215C; color: #CECBF6; }
  .pill-teal { background: #04342C; color: #9FE1CB; }
  .pill-amber { background: #412402; color: #FAC775; }
  .pill-coral { background: #4A1B0C; color: #F5C4B3; }
  .pill-blue { background: #042C53; color: #B5D4F4; }
  .pill-gray { background: #2C2C2A; color: #D3D1C7; }
}
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }
.grid4 { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 8px; }
.stat-card { background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 0.75rem 1rem; }
.stat-label { font-size: 12px; color: var(--color-text-secondary); margin-bottom: 4px; }
.stat-val { font-size: 20px; font-weight: 500; color: var(--color-text-primary); }
.article-row { display: flex; align-items: flex-start; gap: 10px; padding: 8px 0; border-bottom: 0.5px solid var(--color-border-tertiary); }
.article-row:last-child { border-bottom: none; }
.article-num { font-size: 12px; font-weight: 500; color: var(--color-text-tertiary); min-width: 20px; padding-top: 1px; }
.article-title { font-size: 13px; font-weight: 500; color: var(--color-text-primary); }
.article-desc { font-size: 12px; color: var(--color-text-secondary); margin-top: 2px; line-height: 1.5; }
.loop-step { background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 10px 12px; cursor: pointer; transition: background 0.15s; }
.loop-step:hover { background: var(--color-background-info); }
.loop-step.active { border: 1.5px solid var(--color-border-info); background: var(--color-background-info); }
.loop-title { font-size: 13px; font-weight: 500; color: var(--color-text-primary); }
.loop-desc { font-size: 12px; color: var(--color-text-secondary); margin-top: 3px; line-height: 1.5; display: none; }
.loop-step.active .loop-desc { display: block; }
.shell-row { display: flex; align-items: center; gap: 10px; padding: 7px 0; border-bottom: 0.5px solid var(--color-border-tertiary); }
.shell-row:last-child { border-bottom: none; }
.shell-name { font-size: 13px; font-weight: 500; color: var(--color-text-primary); min-width: 110px; }
.shell-fn { font-size: 12px; color: var(--color-text-secondary); }
.layer-block { border-left: 3px solid; padding: 8px 12px; margin-bottom: 6px; border-radius: 0 var(--border-radius-md) var(--border-radius-md) 0; }
.compare-row { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
.compare-cell { padding: 10px 14px; font-size: 13px; border-bottom: 0.5px solid var(--color-border-tertiary); }
.compare-cell:first-child { border-right: 0.5px solid var(--color-border-tertiary); color: var(--color-text-secondary); }
.compare-cell:last-child { color: var(--color-text-primary); font-weight: 500; }
.compare-row:last-child .compare-cell { border-bottom: none; }
.tab-bar { display: flex; gap: 4px; border-bottom: 0.5px solid var(--color-border-tertiary); margin-bottom: 1rem; }
.tab { font-size: 13px; padding: 6px 12px; border-radius: var(--border-radius-md) var(--border-radius-md) 0 0; cursor: pointer; color: var(--color-text-secondary); border: 0.5px solid transparent; border-bottom: none; }
.tab.active { color: var(--color-text-primary); background: var(--color-background-primary); border-color: var(--color-border-tertiary); }
.tab-panel { display: none; }
.tab-panel.active { display: block; }
h2.section-title { font-size: 16px; font-weight: 500; color: var(--color-text-primary); margin-bottom: 0.5rem; }
p.body { font-size: 14px; color: var(--color-text-secondary); line-height: 1.7; margin-bottom: 0.75rem; }
</style>

<h2 class="sr-only" style="position:absolute;left:-9999px">OOI Intelligence repository: full breakdown of documents, architecture, and principles</h2>

<div style="padding: 0.5rem 0 2rem">

<!-- Header -->
<div style="margin-bottom:1.5rem">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
    <span style="font-size:20px;font-weight:500;color:var(--color-text-primary)">OOI Intelligence</span>
    <span class="pill pill-purple">Constitutional Framework</span>
    <span class="pill pill-teal">Execution Architecture</span>
  </div>
  <p class="body" style="margin:0">A framework for intelligence systems that must <em>operate</em> within real-world, consequence-bearing environments — not just describe them.</p>
</div>

<!-- Repo stats -->
<div class="grid4" style="margin-bottom:1.5rem">
  <div class="stat-card"><div class="stat-label">Documents</div><div class="stat-val">4</div></div>
  <div class="stat-card"><div class="stat-label">Constitutional articles</div><div class="stat-val">12</div></div>
  <div class="stat-card"><div class="stat-label">Architecture layers</div><div class="stat-val">8</div></div>
  <div class="stat-card"><div class="stat-label">Governed shells</div><div class="stat-val">8</div></div>
</div>

<!-- Tabs -->
<div class="tab-bar">
  <div class="tab active" onclick="switchTab('overview')">Overview</div>
  <div class="tab" onclick="switchTab('constitution')">Constitution</div>
  <div class="tab" onclick="switchTab('execution')">Execution loop</div>
  <div class="tab" onclick="switchTab('architecture')">Architecture</div>
  <div class="tab" onclick="switchTab('compare')">vs. mainstream AI</div>
</div>

<!-- OVERVIEW TAB -->
<div class="tab-panel active" id="tab-overview">

  <div class="section">
    <div class="section-label">The core problem OOI solves</div>
    <div class="card">
      <p class="body" style="margin-bottom:0.5rem">Modern AI systems excel at <strong style="font-weight:500">representation</strong> — generating language, summarizing, proposing plans. But real environments don't exist in language. They evolve through time, constraint, uncertainty, interaction, and consequence.</p>
      <p class="body" style="margin:0">OOI is a framework for intelligence that can remain coherent while <em>participating</em> in reality, not just describing it.</p>
    </div>
  </div>

  <div class="section">
    <div class="section-label">What "OOI" stands for</div>
    <div class="grid3">
      <div class="card">
        <span class="pill pill-purple" style="margin-bottom:8px;display:inline-block">Operational</span>
        <p style="font-size:13px;color:var(--color-text-secondary);line-height:1.6">Applies to environments where actions change real conditions — delay, uncertainty, coordination, recovery, bounded execution are all native.</p>
      </div>
      <div class="card">
        <span class="pill pill-teal" style="margin-bottom:8px;display:inline-block">Oscillatoric</span>
        <p style="font-size:13px;color:var(--color-text-secondary);line-height:1.6">Reality is dynamic. Stability is not stillness — it is coherence through motion. Drift and recovery are expected system properties, not failures.</p>
      </div>
      <div class="card">
        <span class="pill pill-amber" style="margin-bottom:8px;display:inline-block">Institution</span>
        <p style="font-size:13px;color:var(--color-text-secondary);line-height:1.6">OOI is not a model or product. It is the <em>institutional layer</em> — the governance structure embedded into architecture that makes execution-grade intelligence possible.</p>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">Three documents in the repo</div>
    <div style="display:flex;flex-direction:column;gap:8px">
      <div class="card" style="display:flex;align-items:flex-start;gap:14px">
        <span class="pill pill-purple" style="margin-top:2px;white-space:nowrap">Constitution.md</span>
        <div>
          <div style="font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:3px">The governing layer</div>
          <p style="font-size:12px;color:var(--color-text-secondary);line-height:1.6">12 constitutional articles, 8 governed shells, domain reference builds. The non-negotiable foundation for any OOI-compliant system. 275 lines.</p>
        </div>
      </div>
      <div class="card" style="display:flex;align-items:flex-start;gap:14px">
        <span class="pill pill-teal" style="margin-top:2px;white-space:nowrap">Execution-Intelligence.md</span>
        <div>
          <div style="font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:3px">The operational spec</div>
          <p style="font-size:12px;color:var(--color-text-secondary);line-height:1.6">Full specification of the execution loop, 8-layer architecture, and how intelligence moves from world-state to bounded execution. 196 lines.</p>
        </div>
      </div>
      <div class="card" style="display:flex;align-items:flex-start;gap:14px">
        <span class="pill pill-amber" style="margin-top:2px;white-space:nowrap">Operational-Intelligence.md</span>
        <div>
          <div style="font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:3px">The category framing</div>
          <p style="font-size:12px;color:var(--color-text-secondary);line-height:1.6">High-level framing of the shift from descriptive AI to operational intelligence. Covers the full three-layer stack and design commitments. 158 lines.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">Target domains</div>
    <div style="display:flex;flex-wrap:wrap;gap:6px">
      <span class="pill pill-purple">Healthcare</span>
      <span class="pill pill-teal">Mobility & manufacturing</span>
      <span class="pill pill-amber">Energy & infrastructure</span>
      <span class="pill pill-coral">Education & civic systems</span>
      <span class="pill pill-blue">Knowledge & media</span>
      <span class="pill pill-gray">AI systems design</span>
      <span class="pill pill-gray">Simulation & modeling</span>
      <span class="pill pill-gray">Governance & safety</span>
    </div>
  </div>
</div>

<!-- CONSTITUTION TAB -->
<div class="tab-panel" id="tab-constitution">
  <div class="section">
    <div class="section-label">12 constitutional articles</div>
    <div class="card">
      <div id="articles-list">
        <div class="article-row"><div class="article-num">1</div><div><div class="article-title">Reality precedence</div><div class="article-desc">Symbolic output does not constitute operational validity. What a system says should happen is not proof that it can.</div></div></div>
        <div class="article-row"><div class="article-num">2</div><div><div class="article-title">Human judgment sovereignty</div><div class="article-desc">Humans retain final authority in consequence-bearing domains. Systems must support, not replace, judgment.</div></div></div>
        <div class="article-row"><div class="article-num">3</div><div><div class="article-title">Constraint fidelity</div><div class="article-desc">Constraints are structural requirements — they must be preserved, not optimized around.</div></div></div>
        <div class="article-row"><div class="article-num">4</div><div><div class="article-title">Coherence preservation</div><div class="article-desc">Prefer actions that maintain stability across time, scale, and role.</div></div></div>
        <div class="article-row"><div class="article-num">5</div><div><div class="article-title">Simulation before commitment</div><div class="article-desc">Explore possible actions before executing them when feasible. Prefer explored pathways to untested commitment.</div></div></div>
        <div class="article-row"><div class="article-num">6</div><div><div class="article-title">Legibility requirement</div><div class="article-desc">Operational pathways must be inspectable and understandable. No pathway enters deployment without inspectable structure and risk.</div></div></div>
        <div class="article-row"><div class="article-num">7</div><div><div class="article-title">Drift awareness</div><div class="article-desc">Instability, degradation, and drift are expected conditions — not edge cases.</div></div></div>
        <div class="article-row"><div class="article-num">8</div><div><div class="article-title">Reversibility & interruption</div><div class="article-desc">Actions must be interruptible, reversible, or safely degradable.</div></div></div>
        <div class="article-row"><div class="article-num">9</div><div><div class="article-title">Bounded memory & refinement</div><div class="article-desc">Learning is structured refinement, not uncontrolled accumulation of raw data.</div></div></div>
        <div class="article-row"><div class="article-num">10</div><div><div class="article-title">Non-extractive deployment</div><div class="article-desc">Systems must preserve host sovereignty and identity boundaries. Intelligence must not require unnecessary surrender of data.</div></div></div>
        <div class="article-row"><div class="article-num">11</div><div><div class="article-title">Auditability</div><div class="article-desc">Operational logic must be reviewable by humans and institutions.</div></div></div>
        <div class="article-row"><div class="article-num">12</div><div><div class="article-title">Domain humility</div><div class="article-desc">Systems must not exceed their lawful scope or certainty. No overstating reach or confidence.</div></div></div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">8 governed shells (institutional architecture)</div>
    <div class="card">
      <div class="shell-row"><div class="shell-name">SafeSkin</div><span class="pill pill-coral" style="margin-right:8px">Safety</span><div class="shell-fn">Output governance and safety corridors</div></div>
      <div class="shell-row"><div class="shell-name">SmartSkin</div><span class="pill pill-blue" style="margin-right:8px">Interface</span><div class="shell-fn">Human-legible, role-aware translation</div></div>
      <div class="shell-row"><div class="shell-name">SmartDrift</div><span class="pill pill-amber" style="margin-right:8px">Stability</span><div class="shell-fn">Long-arc drift detection</div></div>
      <div class="shell-row"><div class="shell-name">JitterShell</div><span class="pill pill-purple" style="margin-right:8px">Stability</span><div class="shell-fn">Real-time stability and oscillation control</div></div>
      <div class="shell-row"><div class="shell-name">4D-GR Shell</div><span class="pill pill-teal" style="margin-right:8px">Reasoning</span><div class="shell-fn">Phase-aware, time-evolving reasoning</div></div>
      <div class="shell-row"><div class="shell-name">SmartScience</div><span class="pill pill-green" style="margin-right:8px">Domain</span><div class="shell-fn">Scientific and domain constraint enforcement</div></div>
      <div class="shell-row"><div class="shell-name">SafeVault</div><span class="pill pill-coral" style="margin-right:8px">Security</span><div class="shell-fn">Data, IP, and identity containment</div></div>
      <div class="shell-row"><div class="shell-name">RELSkin</div><span class="pill pill-gray" style="margin-right:8px">Context</span><div class="shell-fn">Cross-context alignment and interpretation</div></div>
    </div>
  </div>
</div>

<!-- EXECUTION LOOP TAB -->
<div class="tab-panel" id="tab-execution">
  <div class="section">
    <div class="section-label">The OOI execution loop — click a step to expand</div>
    <div style="display:flex;flex-direction:column;gap:6px">
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-purple">1</span><div class="loop-title">Structure</div></div>
        <div class="loop-desc">Turn messy, ambiguous real-world input into a usable world-state model. Understand what exists, what roles are present, what conditions apply. This is not summarization — it's world modeling.</div>
      </div>
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-teal">2</span><div class="loop-title">Constrain</div></div>
        <div class="loop-desc">Remove paths that are unsafe, invalid, or impossible under real conditions. Constraints are structural requirements — legal, physical, institutional, procedural. They narrow the action space before anything is tried.</div>
      </div>
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-amber">3</span><div class="loop-title">Simulate</div></div>
        <div class="loop-desc">Test possible actions and trajectories before committing. Explore what could happen across time if a path is taken. Failure is caught in simulation, not in consequence-bearing reality.</div>
      </div>
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-coral">4</span><div class="loop-title">Select</div></div>
        <div class="loop-desc">Choose what is most stable and recoverable — not just most efficient or plausible. The selection criterion is coherence across time and scale, not short-term optimization.</div>
      </div>
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-blue">5</span><div class="loop-title">Execute</div></div>
        <div class="loop-desc">Act in real conditions. Not in symbolic space — in the environment that pushes back. This is where timing, coupling, delay, and physical or institutional boundaries become real.</div>
      </div>
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-purple">6</span><div class="loop-title">Govern</div></div>
        <div class="loop-desc">Monitor, adjust, or interrupt if needed. Governance is not oversight applied after — it is structural and continuous. All actions must remain legible, auditable, and interruptible.</div>
      </div>
      <div class="loop-step" onclick="toggleLoop(this)">
        <div style="display:flex;align-items:center;gap:8px"><span class="pill pill-teal">7</span><div class="loop-title">Learn</div></div>
        <div class="loop-desc">Convert real outcomes into reusable workflows — structured refinement, not raw accumulation. Workflows become the unit of memory. What worked, what degraded, what recovered, and under what conditions.</div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">8 core principles</div>
    <div class="card">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0;border-bottom:0.5px solid var(--color-border-tertiary)">Reality is stateful</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0;border-bottom:0.5px solid var(--color-border-tertiary)">Not all possibilities are operationally real</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0;border-bottom:0.5px solid var(--color-border-tertiary)">Coherence must persist through time</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0;border-bottom:0.5px solid var(--color-border-tertiary)">Constraints enable intelligence</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0;border-bottom:0.5px solid var(--color-border-tertiary)">Simulation precedes commitment</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0;border-bottom:0.5px solid var(--color-border-tertiary)">Workflows are memory</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0">Human legibility is required</div>
        <div style="font-size:13px;color:var(--color-text-secondary);padding:6px 0">Governance is structural</div>
      </div>
    </div>
  </div>
</div>

<!-- ARCHITECTURE TAB -->
<div class="tab-panel" id="tab-architecture">
  <div class="section">
    <div class="section-label">Three-layer stack</div>
    <div style="display:flex;flex-direction:column;gap:6px">
      <div class="layer-block" style="border-color:#534AB7">
        <div style="font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:3px">Constitutional layer — OOI</div>
        <div style="font-size:12px;color:var(--color-text-secondary);line-height:1.6">Human judgment sovereignty · Constraint fidelity · Coherence preservation · Auditability · Non-extractive deployment</div>
      </div>
      <div class="layer-block" style="border-color:#0F6E56">
        <div style="font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:3px">Operational layer — Execution Intelligence</div>
        <div style="font-size:12px;color:var(--color-text-secondary);line-height:1.6">State modeling · Constraint reasoning · Simulation & trajectory testing · Action selection · Real-world execution · Drift detection & recovery · Workflow learning</div>
      </div>
      <div class="layer-block" style="border-color:#BA7517">
        <div style="font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:3px">Deployment layer — Domain Systems</div>
        <div style="font-size:12px;color:var(--color-text-secondary);line-height:1.6">Healthcare · Mobility & manufacturing · Energy & infrastructure · Education & civic systems · Knowledge & media</div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">8-layer architecture stack</div>
    <div class="card">
      <div class="shell-row"><div class="shell-name" style="min-width:130px">1. Ontology</div><div class="shell-fn">World modeling — what exists, what roles are present, what states are active</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">2. Law</div><div class="shell-fn">Constraint modeling — what is allowed, lawful, safe, and institutionally valid</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">3. Simulation</div><div class="shell-fn">Trajectory testing — what could happen if this action is taken</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">4. Control</div><div class="shell-fn">Selection — what should happen, choosing stable and recoverable paths</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">5. Compression</div><div class="shell-fn">Workflow memory — what is learned, distilled into reusable operational structure</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">6. Rendering</div><div class="shell-fn">Human interface — what is seen, legible and role-appropriate output</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">7. Governance</div><div class="shell-fn">Boundedness — what is enforced, monitored, and kept interruptible</div></div>
      <div class="shell-row"><div class="shell-name" style="min-width:130px">8. Deployment</div><div class="shell-fn">What becomes real — domain-specific instantiation of the full stack</div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">Role of language models</div>
    <div class="card">
      <p style="font-size:13px;color:var(--color-text-secondary);line-height:1.6">The framework is explicit: language models function as <strong style="font-weight:500;color:var(--color-text-primary)">semantic interfaces</strong>, not the intelligence substrate. The architecture's substrate is the full Ontology + Law + Simulation + Control stack. LLMs sit at the Rendering layer — they translate operational state into human-legible output, not the other way around.</p>
    </div>
  </div>
</div>

<!-- COMPARE TAB -->
<div class="tab-panel" id="tab-compare">
  <div class="section">
    <div class="section-label">The fundamental shift</div>
    <div class="card" style="padding:0;overflow:hidden">
      <div style="display:grid;grid-template-columns:1fr 1fr;">
        <div style="padding:10px 14px;font-size:12px;font-weight:500;color:var(--color-text-secondary);background:var(--color-background-secondary);border-bottom:0.5px solid var(--color-border-tertiary)">Mainstream AI</div>
        <div style="padding:10px 14px;font-size:12px;font-weight:500;color:var(--color-text-secondary);background:var(--color-background-secondary);border-bottom:0.5px solid var(--color-border-tertiary);border-left:0.5px solid var(--color-border-tertiary)">OOI</div>
      </div>
      <div class="compare-row"><div class="compare-cell">Flow</div><div class="compare-cell">prompt → predict → output</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">situation → model → constrain → simulate → select → execute → govern → learn</div></div>
      <div class="compare-row"><div class="compare-cell">Primary goal</div><div class="compare-cell">Most plausible answer</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">Pathway that can actually work, remain stable, survive reality</div></div>
      <div class="compare-row"><div class="compare-cell">Optimization target</div><div class="compare-cell">Response quality</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">Execution under constraint</div></div>
      <div class="compare-row"><div class="compare-cell">Unit of learning</div><div class="compare-cell">Data points / tokens</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">Reusable operational workflows</div></div>
      <div class="compare-row"><div class="compare-cell">Stability</div><div class="compare-cell">Not a primary concern</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">Native requirement — drift, oscillation, recovery are built-in</div></div>
      <div class="compare-row"><div class="compare-cell">Governance</div><div class="compare-cell">Applied after deployment</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">Embedded in architecture, non-negotiable</div></div>
      <div class="compare-row"><div class="compare-cell">Human role</div><div class="compare-cell">User / prompter</div></div>
      <div class="compare-row"><div class="compare-cell"></div><div class="compare-cell" style="color:var(--color-text-info);border-left:0.5px solid var(--color-border-tertiary)">Sovereign decision-maker, supervisor of coherence</div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-label">Four category shifts</div>
    <div class="grid2">
      <div class="card"><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">From</div><div style="font-size:14px;font-weight:500;color:var(--color-text-secondary);text-decoration:line-through;margin-bottom:6px">Language</div><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">To</div><div style="font-size:14px;font-weight:500;color:var(--color-text-primary)">Execution</div></div>
      <div class="card"><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">From</div><div style="font-size:14px;font-weight:500;color:var(--color-text-secondary);text-decoration:line-through;margin-bottom:6px">Raw data</div><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">To</div><div style="font-size:14px;font-weight:500;color:var(--color-text-primary)">Workflows</div></div>
      <div class="card"><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">From</div><div style="font-size:14px;font-weight:500;color:var(--color-text-secondary);text-decoration:line-through;margin-bottom:6px">Static interaction</div><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">To</div><div style="font-size:14px;font-weight:500;color:var(--color-text-primary)">Dynamic systems</div></div>
      <div class="card"><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">From</div><div style="font-size:14px;font-weight:500;color:var(--color-text-secondary);text-decoration:line-through;margin-bottom:6px">Tools</div><div style="font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px">To</div><div style="font-size:14px;font-weight:500;color:var(--color-text-primary)">Infrastructure</div></div>
    </div>
  </div>
</div>

</div>

<script>
function switchTab(name) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('tab-' + name).classList.add('active');
}
function toggleLoop(el) {
  const wasActive = el.classList.contains('active');
  document.querySelectorAll('.loop-step').forEach(s => s.classList.remove('active'));
  if (!wasActive) el.classList.add('active');
}
</script>

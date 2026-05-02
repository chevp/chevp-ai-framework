import React from 'react';
import Link from '@docusaurus/Link';
import {usePluginData} from '@docusaurus/useGlobalData';

/**
 * Renders a filtered list of plans driven by their frontmatter `status`.
 *
 * Reads all docs from the default content-docs plugin, picks those whose
 * path starts with `/plans/` and whose `phase === 'ctx'` (we want one entry
 * per plan, not per phase), and groups by `frontMatter.status`.
 *
 * Render this component from an MDX page like `plans/index.mdx`:
 *   <PlanList status="active" />
 */
type PlanListProps = {
  status: 'active' | 'finished' | 'archived' | 'deprecated';
};

type DocItem = {
  id: string;
  path: string;
  frontMatter: Record<string, unknown>;
};

type DocsPluginData = {
  versions: Array<{
    docs: DocItem[];
  }>;
};

export default function PlanList({status}: PlanListProps): JSX.Element {
  const data = usePluginData('docusaurus-plugin-content-docs') as
    | DocsPluginData
    | undefined;

  if (!data || !data.versions || data.versions.length === 0) {
    return <p><em>(no plans found)</em></p>;
  }

  const allDocs = data.versions[0].docs;
  const plans = allDocs
    .filter((d) => d.path.includes('/plans/'))
    .filter((d) => d.frontMatter?.phase === 'ctx')
    .filter((d) => d.frontMatter?.status === status);

  if (plans.length === 0) {
    return <p><em>(no {status} plans)</em></p>;
  }

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Created</th>
          <th>Open</th>
        </tr>
      </thead>
      <tbody>
        {plans.map((d) => {
          const id = String(d.frontMatter.plan_id ?? '');
          const slug = String(d.frontMatter.plan_slug ?? '');
          const created = String(d.frontMatter.created ?? '');
          return (
            <tr key={d.id}>
              <td><code>{id}</code></td>
              <td>{slug.replace(/-/g, ' ')}</td>
              <td>{created}</td>
              <td><Link to={d.path}>open →</Link></td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}
